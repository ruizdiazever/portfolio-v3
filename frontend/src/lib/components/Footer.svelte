<script>
    let year = new Date().getFullYear();
    import { onMount } from 'svelte';

    onMount(() => {
        const checkbox = document.querySelector("#checkbox");
        const html = document.querySelector("html");
        const toggleDarkMode = function () {
            if (checkbox.checked == false) {
                html.classList.add("dark")
            } else {
                html.classList.remove("dark");
            }
        }
        toggleDarkMode();
        checkbox.addEventListener("click", toggleDarkMode);
    })
</script>

<footer class="mt-20">
    <div class="flex flex-row footer-div-links my-3">
        <a target="blank" href="https://twitter.com/EverToujours" class="footer-icon icon-sgv">
            <svg class="fill-current" height="24" width="24" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024"><path d="M684.4 158.688c52.88 0 100.621 21.636 134.253 56.372 41.84-8.096 81.28-22.848 116.721-43.28-13.712 41.633-42.88 76.56-80.815 98.656 37.12-4.368 72.656-13.904 105.632-28.16-24.72 35.744-55.84 67.216-91.776 92.368.336 7.632.529 15.344.529 23.023 0 235.728-185.008 507.615-523.312 507.615-103.84 0-200.56-29.631-281.903-80.223a377.607 377.607 0 0 0 43.84 2.527c86.16 0 165.503-28.496 228.463-76.4-80.528-1.376-148.496-53.008-171.808-123.84a188.078 188.078 0 0 0 34.624 3.216c16.72 0 33.008-2.16 48.4-6.256-84.128-16.336-147.536-88.448-147.536-174.93v-2.287c24.816 13.376 53.152 21.408 83.344 22.336-49.376-32.033-81.84-86.56-81.84-148.465 0-32.72 9.089-63.376 24.913-89.632C216.817 299.2 352.337 370.24 505.217 377.712c-3.153-13.025-4.784-26.784-4.784-40.624 0-98.544 82.351-178.4 183.967-178.4zm275.789 83.621h.16-.16zM684.397 94.692c-125.664 0-229.773 91.809-245.806 210.433-102.816-20.656-196.32-75.088-263.504-154.944a63.993 63.993 0 0 0-48.977-22.815 66.23 66.23 0 0 0-5.023.192 64.115 64.115 0 0 0-49.776 30.784 237.575 237.575 0 0 0-34.097 122.656c0 28.848 5.183 56.944 15.008 83.216-10.464 11.632-16.496 26.848-16.496 42.912v2.288c0 62.689 24.784 120.864 65.936 164.464-2.368 10.976-1.84 22.464 1.776 33.472 14.193 43.183 40.033 80.4 73.537 108.75-22.497 5.009-45.712 7.537-69.409 7.537-12.528 0-24.72-.688-36.256-2.097-2.56-.32-5.088-.432-7.632-.432-26.88 0-51.28 16.944-60.336 42.784-9.936 28.32 1.089 59.712 26.56 75.568 94.529 58.817 203.712 89.872 315.712 89.872 364.032 0 583.008-284.976 587.264-563.344a429.584 429.584 0 0 0 78.448-85.152 63.392 63.392 0 0 0 12.96-38.496c0-21.776-10.895-41.024-27.487-52.593 7.184-24.624-1.009-51.28-21.009-67.568-11.68-9.504-26-14.336-40.4-14.336a63.75 63.75 0 0 0-31.968 8.56c-21.152 12.193-43.776 21.841-67.6 28.786-43.105-32.432-96.545-50.496-151.425-50.497z"/></svg>
        </a>
        <a target="blank" href="https://www.linkedin.com/in/everdev/" class="footer-icon icon-sgv">
            <svg class="fill-current" height="24" width="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="m0 0h24v24h-24z" fill="none"/><path d="m12 9.55c.917-.937 2.111-1.55 3.5-1.55a5.5 5.5 0 0 1 5.5 5.5v7.5h-2v-7.5a3.5 3.5 0 0 0 -7 0v7.5h-2v-12.5h2zm-7-3.05a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm-1 2h2v12.5h-2z"/></svg>        </a>
        <a target="blank" href="https://github.com/ruizdiazever" class="footer-icon icon-sgv">
            <svg class="fill-current" height="24" width="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" fill="currentColor"><path d="M21.035 5.257c.91 1.092 1.364 2.366 1.364 3.822 0 5.277-3.002 6.824-5.823 7.279.364.637.455 1.365.455 2.093v3.73c0 .455-.273.728-.637.728a.718.718 0 0 1-.728-.728v-3.73a2.497 2.497 0 0 0-.728-2.093l.455-1.183c2.821-.364 5.733-1.274 5.733-6.187 0-1.183-.455-2.275-1.274-3.185l-.182-.727a4.04 4.04 0 0 0 .09-2.73c-.454.09-1.364.273-2.91 1.365l-.547.09a13.307 13.307 0 0 0-6.55 0l-.547-.09C7.57 2.71 6.66 2.437 6.204 2.437c-.273.91-.273 1.91.09 2.73l-.181.727c-.91.91-1.365 2.093-1.365 3.185 0 4.822 2.73 5.823 5.732 6.187l.364 1.183c-.546.546-.819 1.274-.728 2.002v3.821a.718.718 0 0 1-.728.728.718.718 0 0 1-.728-.728V20.18c-3.002.637-4.185-.91-5.095-2.092-.455-.546-.819-1.001-1.274-1.092-.09-.091-.364-.455-.273-.819.091-.364.455-.637.82-.455.91.182 1.455.91 2 1.547.82 1.092 1.639 2.092 4.095 1.547v-.364c-.09-.728.091-1.456.455-2.093-2.73-.546-5.914-2.093-5.914-7.279 0-1.456.455-2.73 1.365-3.822-.273-1.273-.182-2.638.273-3.73l.455-.364C5.749 1.073 7.023.8 9.66 2.437a13.673 13.673 0 0 1 6.642 0C18.851.708 20.216.98 20.398 1.072l.455.364c.455 1.274.546 2.548.182 3.821z"/></svg>
        </a>
        <a href="/contact" class="footer-icon icon-sgv">
            <svg class="fill-current" height="24" width="24" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><path d="m28 6h-24a2 2 0 0 0 -2 2v16a2 2 0 0 0 2 2h24a2 2 0 0 0 2-2v-16a2 2 0 0 0 -2-2zm-2.2 2-9.8 6.78-9.8-6.78zm-21.8 16v-15.09l11.43 7.91a1 1 0 0 0 1.14 0l11.43-7.91v15.09z"/><path d="m0 0h32v32h-32z" fill="none"/></svg>
        </a>
        <div class="footer-icon icon-sgv">
            <input type="checkbox" name="" id="checkbox" class="hidden" />
            <label for="checkbox" class="cursor-pointer">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"> <circle cx="12" cy="12" r="5" /> <line x1="12" y1="1" x2="12" y2="3" /> <line x1="12" y1="21" x2="12" y2="23" /> <line x1="4.22" y1="4.22" x2="5.64" y2="5.64" /> <line x1="18.36" y1="18.36" x2="19.78" y2="19.78" /> <line x1="1" y1="12" x2="3" y2="12" /> <line x1="21" y1="12" x2="23" y2="12" /> <line x1="4.22" y1="19.78" x2="5.64" y2="18.36" /> <line x1="18.36" y1="5.64" x2="19.78" y2="4.22" /></svg>        
            </label>
        </div>
    </div>
    <div class="footer-ever">
        <span class="text-center">
            &copy <a target="blank" href="https://www.everdev.it" class="mx-auto footer-name">Ever Ruiz Diaz</a> <span>{@html year}</span>
        </span>
    </div>
</footer>

<style>
    footer {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		padding: 12px;
	}
    .footer-icon {
        padding-inline: 6px;
    }

	@media (min-width: 480px) {
		footer {
			padding: 12px 0;
		}
	}
    #checkbox:checked, label {
        transform: translateX(24px);
        transition: transform 0.3s linear;
    }
</style>
