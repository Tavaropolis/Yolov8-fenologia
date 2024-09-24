<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { imgStore } from '../stores/counter'
import axios from 'axios';
import NavBar from "../components/NavBar.vue"

const router = useRouter();
const store = imgStore();
let isLoader = ref(false);
let isActive = ref(true);

//Função para enviar a imagem através do botão
const buttonFileLoad = (async (e) => {
  const fileArray = [...e.target.files];
  uploadImage(await toBase64(fileArray[0]));
});

//Função para enviar a imagem via dragdrop
const dropZoneAction = (async (e) => {
  const dropZoneMsg = document.getElementById("dropZoneMsg");

  if(e.dataTransfer.items[0].kind !== "file") {
    dropZoneMsg.innerText = "Erro: Não é um arquivo";
    throw new Error("Not a file");
  };

  if(e.dataTransfer.items.length > 1) {
    dropZoneMsg.innerText = "Erro: Mais de um arquivo";
    throw new Error("More than one file"); 
  }

  if(e.dataTransfer.items[0].type !== 'image/jpeg' && e.dataTransfer.items[0].type !== 'image/png' && e.dataTransfer.items[0].type !== 'image/webp') {
    dropZoneMsg.innerText = "Erro: Não é uma imagem";
    throw new Error("Not an image"); 
  }

  const fileArray = [...e.dataTransfer.files];
  uploadImage(await toBase64(fileArray[0]));
})


const toBase64 = ((file) => {
  return new Promise ((resolve, reject) => {
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = (() => {
      resolve(reader.result);
    })
    reader.onerror = reject;
  })
})

const uploadImage = (async (image) => {
  try {
    isActive.value = !isActive.value;
    isLoader.value = !isLoader.value;

    const response = await axios({
      method: "POST",
      url: "https://detect.roboflow.com/fenologia-tcc/4",
      params: {
          api_key: "xrqu1dH2PN1Ga56djekh",
          confidence: 80
      },
      data: image,
      headers: {
          "Content-Type": "application/x-www-form-urlencoded",
          "Access-Control-Allow-Origin": "*"
      }
    })
    
    let { width, height } = response.data.image;

    let predictions = response.data.predictions[0].points;

    predictions = predictions.map((point) => {
        return [point.x, point.y];
    })

    const payload = {
      image,
      width,
      height, 
      predictions,
      "confidence": response.data.predictions[0].confidence
    }

    calculateResult(payload);

  } catch(e) {
    isActive.value = !isActive.value;
    isLoader.value = !isLoader.value;
    throw new Error("Failed in request image");
  }
})

const calculateResult = (async (payload) => {
  try {
    const response = await axios({
      method: "POST",
      url: "http://localhost:5000/api/imagetopython",
      headers: {
          "Access-Control-Allow-Origin": "*"
      },
      data: payload
    })

    showResult(response);
  } catch (e) {
    isActive.value = !isActive.value;
    isLoader.value = !isLoader.value;
    throw new Error("Error in calculate image");
  }
})

const showResult = (async (request) => {
  try {
    store.imgResult.base64Img = await request.data.imageBase64;
    store.imgResult.confidence = await request.data.confidence;
    store.imgResult.leaf_index = await request.data.leaf_index;
  
    router.push({path: "/resultado"});
  } catch(e) {
    isActive.value = !isActive.value;
    isLoader.value = !isLoader.value;
  }
})
</script>

<template>
  <NavBar/>
  <main>
    <div v-if="isActive" class="main-container">
      <h1>Como funciona a plataforma?</h1>
      <div>
        <p>Faça o upload de uma imagem através do botão ou arraste na área abaixo</p>
        <input type="file" @change="buttonFileLoad" acept="image/png, image/jpeg, image/webp" name="" id="">
      </div>
      <div class="drop-zone-container">
        <div @drop.prevent="dropZoneAction" @dragenter.prevent @dragover.prevent class="drop-zone">
          <img src="../assets/folder.svg" alt="Pasta de escritório" id="imgFolder">
          <p id="dropZoneMsg">Arraste sua imagem aqui</p>
        </div>
      </div>
    </div>
    <div v-if="isLoader" class="loading-container">
      <img src="../assets/loading.svg" alt="Bola quicando"></img>
    </div>
  </main>
</template>

<style scoped>
.main-container {
  height: 60vh;
  padding: 10px;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
}

.drop-zone-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.drop-zone {
  width: 60vw;
  height: 40vh;
  border: dashed 6px white;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-top: 10vh;
}

.drop-zone:hover {
  border-color: var( --color-text-focus)
}

.drop-zone img{
  width: 10vw;
}

input[type=file] {
  border-radius: 5px;
}

.loading-container {
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>
