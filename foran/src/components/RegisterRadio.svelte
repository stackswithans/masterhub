<script lang="typescript">
    import { onMount, tick } from "svelte";

    export let label: string;
    export let checked: boolean = false;
    export let group: string;
    export let value: string;
    export let id: string
    

    let button: HTMLInputElement;
    let border: HTMLDivElement;
    let toggle: HTMLDivElement;


    const toggleRadio = () => {
        button.checked = !button.checked;
        group = value;
    }

</script>

<div class="container">
    <input {id} bind:group={group}  bind:this={button} {value} type="radio" class="button"/>
    <div on:click={toggleRadio} bind:this={border} class="outer">
        <div bind:this={toggle} class="inner"></div>
    </div>
    <label for="{id}" class="lab">{label}</label>
</div>

<style>
    .container{
        display: flex;
        align-items: center;
        gap: 0.5rem;
        width: fit-content;  
    }

    .container:hover{
        cursor: pointer;
    }

    input{
        position: absolute;
        width: 1px;
        height: 1px;
        padding: 0;
        margin: -1px;
        overflow: hidden;
        white-space: nowrap;
        border-width: 0;
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

    input:checked ~ .outer{
        border-color: var(--color-2);
    }

    input:checked ~ .outer .inner{
        background-color: var(--color-2);
    }

    .lab{
        color: var(--color-3);
        font-family: "Roboto";
        font-size: 0.9rem;
    }

</style>
