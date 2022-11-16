<script>
    import axios from "axios";
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
        <hr class="divisor mx-auto">
        <div class="cv-container mt-3">
            <button class="cv-btn">Curriculum</button>
            <button class="cv-btn">Certifications</button>
        </div>
    </div>

    <!-- BLOG -->
    <div class="mb-5 mt-10">
        <h2 class="text-2xl mb-5 text-center">Blog</h2>
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

    .skill-container, .cv-container {
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        justify-content: center;
        align-items: center;
    }

    .skill-btn {
        margin-inline: 2px;
    }

    .cv-btn {
        margin-inline: 5px;
        margin-bottom: 0.3rem;
        padding: 0.2em 1em;
        border-radius: 99999px;
        font-weight: 700;
        font-size: 20px;
        font-family: "Inter var", "Inter", -apple-system, BlinkMacSystemFont, "Helvetica", "Cantarell", sans-serif;
        line-height: 1.6;
        letter-spacing: -0.03em;
        word-spacing: -0.03em;
    }

    .divisor {
        max-width: 200px;
    }
</style>
