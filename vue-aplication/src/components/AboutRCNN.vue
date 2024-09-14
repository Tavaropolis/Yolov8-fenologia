<script setup>

</script>

<template>
    <h2>O que é R-CNN?</h2>
    <p>&emsp;CNN (Convolutional Neural Networks) é uma forma de se obter a classificação de uma imagem, através de redes neurais profundas, o deeplearning. O CNN se utiliza de "kernels" formados por fórmulas matemáticas, que analisam uma determinada matriz de pixels por vez, até passar por toda a imagem. Esses kernels tem a capacidade de identificar certas características da imagem, por exemplo, um pode identidicar pontas, ou kernel pode identificar blur, e assim por diante. Após o resultado obtido o CNN classifica a imagem conforme o treinamento aplicado. Por exemplo: alimenta-se o CNN com várias imagens classificadas como sendo um cachorro, o CNN aprende as características que formam esse tipo de imagem, e ao ser alimentado com outra imagem, ele saberá classificar se é um cachorro ou não.</p>
    <p>&emsp;Este modelo entretanto tem suas limitações, sendo relativamente desafiador identificar quando a mais de um mesmo objeto na imagem e classifica-la. Para resolver esses desafios é utilizado a abordagem R-CNN. A principal diferença desta abordagem é que há uma classificação de zonas de interesse por padrões na imagem, antes da aplicação dos kernels.</p>
</template>

<style scoped>
p {
    padding: 10px;
}
</style>