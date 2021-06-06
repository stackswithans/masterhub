<script lang="typescript">
    export let text = "";
    export let type = "button";
    export let arrow = true;
</script>

<button on:click class="button" type="{type}">
    {#if arrow}
        <div></div>
        {text}
        <i class="fas fa-arrow-right"></i>
    {:else}
        <div></div>
        {text}
        <div></div>
    {/if}
</button>

<style>
    .button{
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 1rem;
        font-family: "Roboto";
        font-size: 1.1rem;
        color: white;
        background-color: var(--color-1);
        border: 0;
        width: 19.5em; /*height-width ratio: 0.111;*/
        height: 1.80rem;
        box-shadow: 0px 0px 1rem -10px black;
        border-radius: 25px;
    }

    .button:hover{
        cursor: pointer;
        opacity: 0.8;
    }

    .button:active{
        background-color: var(--color-1);
    }
</style>
