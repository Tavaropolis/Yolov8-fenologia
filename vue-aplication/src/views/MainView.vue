<script setup>
import NavBar from "../components/NavBar.vue"

const dropZoneOpenFolder = (() => {
  const imgFolder = document.getElementById("imgFolder");
  imgFolder.setAttribute("src", "../assets/folderOpen.svg");
});

const dropZoneCloseFolder = (() => {
  const imgFolder = document.getElementById("imgFolder");
  imgFolder.setAttribute("src", "../assets/folder.svg");
});

const dropZoneAction = ((e) => {
  const dropZoneMsg = document.getElementById("dropZoneMsg");

  if(e.dataTransfer.items[0].kind !== "file") {
    dropZoneMsg.innerText = "Erro: Não é um arquivo";
    throw new Error("Not a file");
  };

  if(e.dataTransfer.items.length > 1) {
    dropZoneMsg.innerText = "Erro: Mais de um arquivo";
    throw new Error("More than one file"); 
  }

  if(e.dataTransfer.items[0].type !== 'image/jpeg' && e.dataTransfer.items[0].type !== 'image/png') {
    dropZoneMsg.innerText = "Erro: Não é uma imagem";
    throw new Error("Not an image"); 
  }

  const fileArray = [...e.dataTransfer.files];
  uploadImage(fileArray[0]);
})

const uploadImage = ((file) => {
  console.log(file);
})

</script>

<template>
  <NavBar/>
  <main>
    <h1>Como funciona a plataforma?</h1>
    <p>Faça o upload de uma imagem através do botão ou arraste na área abaixo</p>
    <input type="file" name="" id="">
    <div class="drop-zone-container">
      <div @drop.prevent="dropZoneAction" @dragenter.preven @dragover.prevent class="drop-zone">
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
