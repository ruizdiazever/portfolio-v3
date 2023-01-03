<script>
    import logo from "$lib/images/logo.webp";

    function closeMenu () {
        const status = document.querySelector("#dropdown-menu");
        const action =  status.classList.add("hidden")
        action.addEventListener("click", action);
    }

    function openMenu () {
        const status = document.querySelector("#dropdown-menu");
        const action =  status.classList.remove("hidden")
        action.addEventListener("click", action);
    }
</script>

<div class="relative px-4 pt-3 sm:px-6 lg:px-8">
    <nav class="relative flex items-center justify-between sm:h-10 lg:justify-start" aria-label="Global">
        <div class="flex flex-shrink-0 flex-grow items-center lg:flex-grow-0">
            <div class="flex w-full items-center justify-between md:w-auto">
                <div class="-mr-2 flex items-center md:hidden">
                    <button on:click={() => openMenu()} type="button" class="header-dropdown-btn" aria-expanded="false">
                        <span class="sr-only">Open main menu</span>
                        <!-- Heroicon name: outline/bars-3 -->
                        <svg class="h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
                        </svg>
                    </button>
                </div>
            </div>
        </div>
    </nav>
</div>

<!-- MENU -->
<div id="dropdown-menu" class="header-dropdown-menu hidden">
    <div class="overflow-hidden rounded-lg dark:text-green-300 dark:hover:text-green-200 dark:bg-[#28292a] bg-emerald-50 shadow-md ring-1 ring-black ring-opacity-5">
        <div class="flex items-center justify-between px-5 pt-4">
            <div>
            <img class="h-8 w-auto" src={logo} alt="">
            </div>
            <div class="-mr-2">
            <button on:click={() => closeMenu()} type="button" class="header-dropdown-btn">
                <span class="sr-only">Close main menu</span>
                <!-- Heroicon name: outline/x-mark -->
                <svg class="h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
                <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
                </svg>
            </button>
            </div>
        </div>
        <div class="space-y-1 px-2 pt-2 pb-3">
            <a href="/" class="header-dropdown-menu-url">Home</a>

            <a href="/projects" class="header-dropdown-menu-url">Projects</a>


            <!-- <a href="/blog" class="header-dropdown-menu-url">Blog</a> -->
        </div>
        <div class="icon-footer">
            <a href="https://github.com/ruizdiazever" class="px-5 py-3 font-medium">
                <svg class="fill-current icon-sgv" height="24" width="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" fill="currentColor"><path d="M21.035 5.257c.91 1.092 1.364 2.366 1.364 3.822 0 5.277-3.002 6.824-5.823 7.279.364.637.455 1.365.455 2.093v3.73c0 .455-.273.728-.637.728a.718.718 0 0 1-.728-.728v-3.73a2.497 2.497 0 0 0-.728-2.093l.455-1.183c2.821-.364 5.733-1.274 5.733-6.187 0-1.183-.455-2.275-1.274-3.185l-.182-.727a4.04 4.04 0 0 0 .09-2.73c-.454.09-1.364.273-2.91 1.365l-.547.09a13.307 13.307 0 0 0-6.55 0l-.547-.09C7.57 2.71 6.66 2.437 6.204 2.437c-.273.91-.273 1.91.09 2.73l-.181.727c-.91.91-1.365 2.093-1.365 3.185 0 4.822 2.73 5.823 5.732 6.187l.364 1.183c-.546.546-.819 1.274-.728 2.002v3.821a.718.718 0 0 1-.728.728.718.718 0 0 1-.728-.728V20.18c-3.002.637-4.185-.91-5.095-2.092-.455-.546-.819-1.001-1.274-1.092-.09-.091-.364-.455-.273-.819.091-.364.455-.637.82-.455.91.182 1.455.91 2 1.547.82 1.092 1.639 2.092 4.095 1.547v-.364c-.09-.728.091-1.456.455-2.093-2.73-.546-5.914-2.093-5.914-7.279 0-1.456.455-2.73 1.365-3.822-.273-1.273-.182-2.638.273-3.73l.455-.364C5.749 1.073 7.023.8 9.66 2.437a13.673 13.673 0 0 1 6.642 0C18.851.708 20.216.98 20.398 1.072l.455.364c.455 1.274.546 2.548.182 3.821z"/></svg>
            </a>
            <div>
                <input type="checkbox" name="" id="checkbox" class="hidden" />
                <label for="checkbox" class="cursor-pointer">
                    <svg class="fill-current icon-sgv" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"> <circle cx="12" cy="12" r="5" /> <line x1="12" y1="1" x2="12" y2="3" /> <line x1="12" y1="21" x2="12" y2="23" /> <line x1="4.22" y1="4.22" x2="5.64" y2="5.64" /> <line x1="18.36" y1="18.36" x2="19.78" y2="19.78" /> <line x1="1" y1="12" x2="3" y2="12" /> <line x1="21" y1="12" x2="23" y2="12" /> <line x1="4.22" y1="19.78" x2="5.64" y2="18.36" /> <line x1="18.36" y1="5.64" x2="19.78" y2="4.22" /></svg>        
                </label>
            </div>
        </div>
    </div>
</div>

<style>
    .icon-footer {
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        justify-content: center;
        align-items: center;
    }
</style>
