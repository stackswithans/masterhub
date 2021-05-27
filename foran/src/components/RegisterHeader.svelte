<script lang="typescript">
    import { onMount } from "svelte";
    export let description: string = "";
    export let step: number = 1;
    let loader; 
    onMount(() => {
        loader.style.width = `${(105/3) * step}%`;
    });
</script>

<div class="main">
    <label class="description">{description}</label>
    <div bind:this={loader} class="loader"></div>
</div>

<style>
    .main{
        padding: 1rem;
        width: fit-content;
    }

    .description{
        position: relative;
        width: 100%;
        font-family: "Roboto";
        font-weight: bold;
        font-size: 1.4em;
        color: var(--color-3);
    }

    .loader{
        height: 0.5rem;
        border-radius: 5px;
        background-color: var(--color-1);
        margin-top: 0.5rem;
    }
</style>
