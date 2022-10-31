<script>
    import axios from "axios";
    import renato from "$lib/images/renato.jpg";
    import pawel from "$lib/images/pawel.jpg";
    import { secret } from '$lib/js/store.js';
    let name = "404";

    async function getData() {
        const path = "http://127.0.0.1:8000/about";
        let headers = { headers: { "Content-Type": "application/json" } };
        await axios.get(path, headers).then((response) => {
            name = response.data.name;
        });
    }
</script>

<main>
    <!-- TITLE -->
    <div class="container mx-auto max-w-xl">
        <h1 class="title-name">Ever Ruiz Diaz</h1>
        <p class="mt-2 text-lg text-center">Software Developer Engineer</p>
        <div class="scale-75 skill-container">
            <button class="skill-btn">Rust</button>
            <button class="skill-btn">Python</button>
            <button class="skill-btn">GNU/Linux</button>
            <button class="skill-btn">Bash Scripting</button>
            <button class="skill-btn">Git</button>
            <button class="skill-btn">Docker</button>
            <button class="skill-btn">PostgreSQL</button>
            <button class="skill-btn">OracleDB</button>
            <button class="skill-btn">Svelte</button>
            <button class="skill-btn">GraphQL</button>
            <button class="skill-btn">Axios</button>
            <button class="skill-btn">Tailwind CSS</button>
            <button class="skill-btn">Bootstrap</button>
            <button class="skill-btn">Mkdocs</button>
            <button class="skill-btn">FastAPI</button>
        </div>
    </div>

    <!-- CARD -->
    <div class="container max-w-2xl mx-auto lg:columns-2 my-5">
        <div class="card">
            <div class="card-header">
                <img src={renato} class="card-img w-full rounded-[24px]" alt="Logo">
            </div>
            <div class="card-body py-6">
                <a href="www.everdev.it"><h2 class="text-xl text-center">Curriculum</h2></a>
                <p class="mt-2 text-center">See or download my curriculum</p>
            </div>
        </div>
        <div class="card">
            <div class="card-header">
                <img src={pawel} class="card-img w-full rounded-[24px]" alt="Logo">
            </div>
            <div class="card-body py-6">
                <a href="www.everdev.it"><h2 class="text-xl text-center">Certifications</h2></a>
                <p class="mt-2 text-center">Some of my certifications</p>
            </div>
        </div>
    </div>

    <!-- BLOG -->
    <div class="mb-5 mt-10">
        <h2 class="text-2xl mb-5 text-center">Roadmap</h2>
        <ul>
            <li class="blog-li pl-5 text-justify mx-auto max-w-2xl rounded-full py-2 mb-2"><span class="blog-li-span">29/10/22<span><span class="ml-5 blog-li-span-2">Today is Svelte day</span></li>
            <li class="blog-li pl-5 text-justify mx-auto max-w-2xl rounded-full py-2 mb-2"><span class="blog-li-span">29/10/22<span><span class="ml-5 blog-li-span-2">Python y todas las droguitas</span></li>
            <li class="blog-li pl-5 text-justify mx-auto max-w-2xl rounded-full py-2 mb-2"><span class="blog-li-span">29/10/22<span><span class="ml-5 blog-li-span-2">Today is Svelte day</span></li>
        </ul>
    </div>
</main>

<style>
    .title-name {
        text-align: center;
        letter-spacing: -.05em;
        font-size: 3.5rem;
        padding-top: 2.25rem;
        font-weight: 700;
    }
    .card-img {
        max-height: 120px;
    }

    .skill-container {
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        justify-content: center;
        align-items: center;
    }

    .skill-btn {
        margin-inline: 2px;
    }
</style>
