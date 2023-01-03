<script>
    import { secret } from '$lib/js/store.js';
    let collapsed = true;
    let pathCurriculum = import.meta.env.VITE_API_FILE
</script>

<main>
    <!-- TITLE -->
    <div class="container mx-auto max-w-xl">
        <h1 class="title-name">Ever Ruiz Diaz</h1>
        <p class="mt-2 text-lg text-center">Software Developer Engineer</p>
        <div class="scale-75 skill-container">
            <button class="skill-btn" on:click={() => window.open('https://www.rust-lang.org/')}>Rust</button>
            <button class="skill-btn" on:click={() => window.open('https://www.python.org/')}>Python</button>
            <button class="skill-btn" on:click={() => window.open('https://www.linuxfoundation.org/')}>GNU/Linux</button>
            <button class="skill-btn" on:click={() => window.open('https://en.wikipedia.org/wiki/Bash_(Unix_shell)')}>Bash Scripting</button>
            <button class="skill-btn" on:click={() => window.open('https://git-scm.com/')}>Git</button>
            <button class="skill-btn" on:click={() => window.open('https://www.docker.com/')}>Docker</button>
            <button class="skill-btn" on:click={() => window.open('https://www.postgresql.org/')}>PostgreSQL</button>
            <button class="skill-btn" on:click={() => window.open('https://redis.io/')}>RedisDB</button>
            <button class="skill-btn" on:click={() => window.open('https://www.mongodb.com/')}>MongoDB</button>
            <button class="skill-btn" on:click={() => window.open('https://svelte.dev/')}>Svelte</button>
            <button class="skill-btn" on:click={() => window.open('https://graphql.org/')}>GraphQL</button>
            <button class="skill-btn" on:click={() => window.open('https://tailwindcss.com/')}>Tailwind CSS</button>
            <button class="skill-btn" on:click={() => window.open('https://getbootstrap.com/')}>Bootstrap</button>
            <button class="skill-btn" on:click={() => window.open('https://squidfunk.github.io/mkdocs-material/')}>Mkdocs</button>
            <button class="skill-btn" on:click={() => window.open('https://fastapi.tiangolo.com/')}>FastAPI</button>
            <button class="skill-btn" on:click={() => window.open('https://tokio.rs/blog/2021-07-announcing-axum')}>Axum</button>
        </div>
        <hr class="divisor mx-auto">
        <div class="cv-container mt-3">
            <button class="cv-btn" on:click={() => window.open(pathCurriculum)}>Curriculum</button>
            <button class="cv-btn">Certifications</button>
        </div>
        <div>
            
        </div>

        
        <div class="mt-10" >
            <p class="mb-2 transition-all opacity-100">Hola, I'm a developer and a strong supporter of Open Source passionate about modern architectures, software solutions and sciences.</p>
            <p class="{!collapsed ? 'mb-2' : ''} {collapsed ?'transition-all opacity-75' : ''}">I have experience in Python, Bash Scripting, GNU/Linux, Git, Docker, PostgreSQL, OracleDB, Tailwind CSS, JavaScript (a little bit), Bootstrap, Mkdocs and FastAPI.</p>
            <p class="{collapsed ?'transition-all opacity-50' : ''} mt-2">Currently focused on Rust (my favorite language), Svelte and GraphQL.</p>
            <p class="{!collapsed ? 'mb-2' : ''}">
                {#if !collapsed}
                    I have worked in the aerospace industry and thus fulfilled one of my childhood dreams.
                    My next goals are to develop innovative software with the power of Rust and 
                    to collaborate more actively with it and Python to the world of open source software... 
                    another dream to achieve would be a photo with Linus Torvalds.
                {/if}
            </p>
            <span class="collapse-btn-container">
                <button class="collapse-btn" on:click={() => (collapsed = !collapsed)}>
                    {#if collapsed}
                        <small>Expand text</small>
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-4 h-4 mx-auto">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 8.25l-7.5 7.5-7.5-7.5" />
                        </svg>
                    {:else}
                        <small>Collapse text</small>
                        <svg  xmlns="http://www.w3.org/2000/svg" role="img" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-4 h-4 mx-auto">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 15.75l7.5-7.5 7.5 7.5" />
                        </svg>
                    {/if}
                </button>
            </span>
        </div>
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

    .skill-container, .cv-container, .collapse-btn-container {
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
