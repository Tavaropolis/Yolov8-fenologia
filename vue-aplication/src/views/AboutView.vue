<script setup>
import NavBar from "../components/NavBar.vue";

</script>

<template>
    <NavBar/>
    <main>
        <section class="buffer">
            <h2>Como funciona a aplicação?</h2>
            <p>Esta aplicação calcula a intensidade foliar de </p>
        </section>
        <div class="parallax" id="img-1"></div>
        <section class="buffer">
            <h2>O que é IA?</h2>
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Provident ab dignissimos pariatur neque ipsum corporis numquam voluptatem ex. Cupiditate neque earum quisquam similique ducimus architecto cumque autem, quia nemo minus.</p>
        </section>
        <section class="buffer">
            <h2>O que é fenologia?</h2>
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Provident ab dignissimos pariatur neque ipsum corporis numquam voluptatem ex. Cupiditate neque earum quisquam similique ducimus architecto cumque autem, quia nemo minus.</p>
        </section>
        <section class="buffer">
            <h2>O que é fenologia?</h2>
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Provident ab dignissimos pariatur neque ipsum corporis numquam voluptatem ex. Cupiditate neque earum quisquam similique ducimus architecto cumque autem, quia nemo minus.</p>
        </section>
        <section class="buffer">
            <h2>O que é R-CNN?</h2>
            <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Culpa nemo, corporis tenetur officia doloribus vel provident ad? Molestiae aperiam provident, harum ut nostrum tempora repellendus eum expedita animi, quas tenetur?</p>
        </section>
        <div class="parallax" id="img-2"></div>
        <section class="buffer">
            <h2>Referências Bibliográficas</h2>
        </section>
    </main>
</template>

<style scoped>
.buffer {
    text-align: justify;
    max-width: 100%;
}

.parallax{
    min-height: 50vh;
    max-width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;

    /*  this is where the magic happens:  */
    background-attachment: fixed;
    background-position: center;
    background-size: cover;
}

#img-1{
    background-image: url("../assets/flowerthree.jpg");
}

#img-2{
    background-image: url("../assets/jungleplants.jpg");
}
</style>