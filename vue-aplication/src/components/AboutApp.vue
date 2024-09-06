<script setup>
import { RouterLink } from 'vue-router';

</script>

<template>
    <h2>Como funciona a aplicação?</h2>
    <p>&emsp;Esta aplicação calcula a intensidade da presença foliar em espécies árboreas de acordo com a escala de Founier. Esta escala é utilizada em muitos trabalhos das áreas de botânica e fenologia, ela consiste em classificar um atríbutocomo presença de folhas ou presença de flores, em uma escala de 0 a 4, em relação a presença e a área total da copa da árvore. Por exemplo: se não houver folhas na copa de uma árvore, ela seria indíce 0, se houvesse entre 1% a 25%, ela seria indíce 1, de 26% a 50%, indíce 2, 51% a 75% indice 3 e por fim 76% a 100% indíce 4.</p>
    <p>&emsp;Este projeto consiste em receber uma imagem de árvore do usuário, e envia-la para um modelo de Inteligência Artificial treinado na arquitetura Mask-RCNN via linguagem Python. Ela analisará a imagem e retornará o indíce de Fournier correspondente. </p>
    <p>Basta seguir os seguintes passos: </p>
    <ul>
        <li>Acesse a aba <RouterLink to="/">Home</RouterLink></li>
        <li>Faça o upload da imagem ou arraste para a área de drop</li>
        <li>Aguarde o resultado ainda na aba principal</li>
    </ul>
</template>

<style scoped>
p {
    padding: 10px;
}
</style>