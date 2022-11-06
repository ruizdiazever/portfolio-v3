<script>
    import axios from "axios";
    import renato from "$lib/images/renato.jpg";
    import pawel from "$lib/images/pawel.jpg";
    import Loader from "$lib/components/Loader.svelte";
    import { secret } from '$lib/js/store.js';

    let blog = [];
    let path = import.meta.env.VITE_API_ENPOINT
    let showLoader = true

    const graphqlQuery = {
        "operationName": "Blog",
        "query": `query Blog { blog { title, date } }`,
        "variables": {}
    };

    async function getBlog() {
        let headers = { headers: { "Content-Type": "application/json" } };
        try {
            await axios.post(path, graphqlQuery, headers).then((response) => {
                blog = response.data.data.blog;
                showLoader = false;
            });
        } catch (error) {
            console.log(error.message);
        }
    }
    getBlog();
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
                <a href="https://www.everdev.it" target="blank"><h2 class="text-xl text-center">Curriculum</h2></a>
                <p class="mt-2 text-center">See or download my curriculum</p>
            </div>
        </div>
        <div class="card">
            <div class="card-header">
                <img src={pawel} class="card-img w-full rounded-[24px]" alt="Logo">
            </div>
            <div class="card-body py-6">
                <a href="https://www.everdev.it" target="blank"><h2 class="text-xl text-center">Certifications</h2></a>
                <p class="mt-2 text-center">Some of my certifications</p>
            </div>
        </div>
    </div>

    <!-- BLOG -->
    <div class="mb-5 mt-10">
        <h2 class="text-2xl mb-5 text-center">Roadmap</h2>
        {#if showLoader}
            <Loader />
        {:else}
            <ul>
                {#each blog as item}
                <li class="blog-li"><code class="blog-li-span text-sm">{item.date}</code><span class="ml-5 blog-li-span-2">{item.title}</span></li>
                {/each}
            </ul>
        {/if}
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
