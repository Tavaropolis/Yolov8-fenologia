<script setup>
import { ref } from 'vue';
import { useBase64Img } from '../stores/counter'
import NavBar from "../components/NavBar.vue"

const store = useBase64Img();
const mainImg = ref(store.base64Img);

</script>

<template>
    <NavBar/>
    <div class="result-container">
        <a :href="mainImg" download>
            <img :src="mainImg" alt="imagem enviada pelo usuário">
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
}
</style>