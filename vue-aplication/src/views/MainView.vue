<script setup>
import { useRouter } from 'vue-router';
import { useBase64Img } from '../stores/counter'
import axios from 'axios';
import NavBar from "../components/NavBar.vue"

const router = useRouter();
const store = useBase64Img();

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


const toBase64 = ( (file) => {
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
    const response = await axios({
      method: "POST",
      url: "https://detect.roboflow.com/fenologia-tcc/3",
      params: {
          api_key: "xrqu1dH2PN1Ga56djekh"
      },
      data: image,
      headers: {
          "Content-Type": "application/x-www-form-urlencoded",
          "Access-Control-Allow-Origin": "*"
      }
    })

    calculateResult(image);

  } catch(e) {
    console.log(e)
    throw new Error("Failed in request image");
  }
})

const calculateResult = (async (image) => {
  try {
    const response = await axios({
      method: "POST",
      url: "https://deteccao-floracao-flask-python.vercel.app/imagetopython",
      headers: {
          "Access-Control-Allow-Origin": "*"
      },
      data: {
        "image": image 
      }
    })

    showResult(response);
  } catch (e) {
    console.log(e)
  }
})

const showResult = (async (request) => {
  store.base64Img = await request.data.imageBase64;

  router.push({path: "/resultado"});
})
</script>

<template>
  <NavBar/>
  <main>
    <h1>Como funciona a plataforma?</h1>
    <p>Faça o upload de uma imagem através do botão ou arraste na área abaixo</p>
    <input type="file" @change="buttonFileLoad" acept="image/png, image/jpeg, image/webp" name="" id="">
    <div class="drop-zone-container">
      <div @drop.prevent="dropZoneAction" @dragenter.prevent @dragover.prevent class="drop-zone">
        <img src="../assets/folder.svg" alt="Pasta de escritório" id="imgFolder">
        <p id="dropZoneMsg">Arraste sua imagem aqui</p>
      </div>
    </div>
  </main>
</template>

<style scoped>
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
  align-items: center
}

.drop-zone img{
  width: 10vw;
}
</style>
