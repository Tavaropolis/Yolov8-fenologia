<script setup>
import { ref } from 'vue';
import { useBase64Img } from '../stores/counter'

const store = useBase64Img();
const mainImg = ref(store.base64Img);

</script>

<template>
    <img :src="mainImg" alt="imagem enviada pelo usuário">
</template>

<style scoped>

</style>