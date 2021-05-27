<script lang="typescript">
    import {onMount} from "svelte";

    export let label: string;
    export let name: string;
    export let checked: boolean = false;
    let button: HTMLInputElement;

    onMount(() => {
        if(checked) button.checked = true;
    });

</script>

<div class="container">
    <div class="outer">
      <div class="inner"></div>
    </div>
    <input id="input" bind:this={button} name={name} type="radio" class="button" hidden/>
    <label for="" class="lab">{label}</label>
</div>

<style>
    .container{
        display: flex;
        align-items: center;
        gap: 0.5rem;
        width: fit-content;  
    }

    .outer{
        display: flex;
        align-items: center;
        justify-content: center;
        width: 1rem;
        height: 1rem;
        border: 1px solid var(--color-11);
        border-radius: 50%;
        transition: border-color 0.5s ease;
    }

    .inner{
        width: 0.5rem;
        height: 0.5rem;
        border-radius: 50%;
        transition: background-color 0.5s ease;
    }

    .outer:hover{
        border-color: var(--color-2);
    }

    .outer:hover > .inner{
        background-color: var(--color-2);
    }

    .lab{
        color: var(--color-3);
        font-family: "Roboto";
        font-size: 0.9rem;
    }

    input{
        display: none;
    }
</style>
