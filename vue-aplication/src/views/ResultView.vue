<script setup>
import { ref, onMounted } from 'vue';
import { imgStore } from '../stores/counter'
import NavBar from "../components/NavBar.vue"

const store = imgStore();
const base64Img = ref(store.imgResult.base64Img);
const confidence = ref(`${store.imgResult.confidence.toFixed(4) * 100}%`);
const leaf_index = ref(`${store.imgResult.leaf_index}%`);
const fournier_index = ref(0);

onMounted(() => {
    if(store.imgResult.leaf_index == 0) {
        fournier_index.value = 0;
    } else if (store.imgResult.leaf_index > 0 && store.imgResult.leaf_index <= 25) {
        fournier_index.value = 1;
    } else if (store.imgResult.leaf_index > 25 && store.imgResult.leaf_index <= 50) {
        fournier_index.value = 2; 
    } else if (store.imgResult.leaf_index > 50 && store.imgResult.leaf_index <= 75) {
        fournier_index.value = 3; 
    } else if (store.imgResult.leaf_index > 75 && store.imgResult.leaf_index <= 100) {
        fournier_index.value = 4; 
    }
})

</script>

<template>
    <NavBar/>
    <div class="result-container">
        <div class="info-container">
            <p>Confiança: {{ confidence }}</p>
            <p>Intensidade foliar: {{ leaf_index }}</p>
            <p>Índice Fournier: {{ fournier_index }}</p>
        </div>
        <p><span>(Você pode baixar a imagem clicando nela)</span></p>
        <a :href="base64Img" download>
            <img :src="base64Img" alt="imagem enviada pelo usuário">
        </a>
    </div>
</template>

<style scoped>
.result-container {
    min-height: 80vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin: 10px
}

.info-container {
    width: 15vw;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;

}
span {
    font-style: italic;
    font-size: 0.8rem;
}

img {
    max-width: 50vw;
}
</style>