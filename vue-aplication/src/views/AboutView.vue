<script setup>
import NavBar from "../components/NavBar.vue";

</script>

<template>
    <NavBar/>
    <main>
        <div class="buffer">
            <h2>Como funciona a aplicação?</h2>
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quo dicta deleniti nihil similique dolor at ut excepturi. Nemo adipisci ratione alias, fugit voluptates perferendis neque ex iusto autem voluptatibus debitis corporis dolorem odit ullam. Rerum, ea saepe. Quos tempora consequuntur cupiditate molestias amet tenetur corporis architecto. Nisi iste debitis, consequuntur repudiandae eius nesciunt suscipit blanditiis! Consequatur tenetur beatae, sed nisi eius enim libero porro necessitatibus. Harum voluptatem, hic eos, earum soluta nihil quas numquam eaque dolores facere animi eveniet alias laudantium ipsam temporibus quisquam ut? Non tenetur illum hic sit mollitia quo aut exercitationem excepturi magnam expedita obcaecati facere modi rerum, quod rem voluptatem dicta. Perspiciatis debitis deserunt sapiente numquam quaerat repellat minus fugit a exercitationem deleniti laboriosam repellendus nisi sed ea animi cupiditate facere consectetur, iste similique eos architecto dolorum, magni sequi! Magni obcaecati facilis eaque, qui accusamus minima temporibus. Quaerat sed officia soluta ea porro! Veritatis, reprehenderit consequatur! Consequatur, ut nisi dicta beatae cum, iure architecto suscipit adipisci fugit, libero voluptate quam dolore! Et placeat hic mollitia iure similique atque, harum officiis beatae eos ea ullam amet reprehenderit repudiandae illo inventore? Reprehenderit, voluptas minus aliquam illum quis iure quidem. Illum impedit consectetur et ipsam esse inventore sed quia.
            </p>
        </div>
        <div class="parallax"></div>
        <div class="buffer">
            <h2>O que é IA?</h2>
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Provident ab dignissimos pariatur neque ipsum corporis numquam voluptatem ex. Cupiditate neque earum quisquam similique ducimus architecto cumque autem, quia nemo minus.</p>
            <h2>O que é fenologia?</h2>
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Provident ab dignissimos pariatur neque ipsum corporis numquam voluptatem ex. Cupiditate neque earum quisquam similique ducimus architecto cumque autem, quia nemo minus.</p>
            <h2>O que é fenologia?</h2>
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Provident ab dignissimos pariatur neque ipsum corporis numquam voluptatem ex. Cupiditate neque earum quisquam similique ducimus architecto cumque autem, quia nemo minus.</p>
            <h2>O que é R-CNN?</h2>
            <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Culpa nemo, corporis tenetur officia doloribus vel provident ad? Molestiae aperiam provident, harum ut nostrum tempora repellendus eum expedita animi, quas tenetur?</p>
        </div>
        <div class="parallax"></div>
        <h2>Referências Bibliográficas</h2>
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

  background-image: url("../assets/flowerthree.jpg");
  background-position: center;
  background-size: cover;
}

</style>