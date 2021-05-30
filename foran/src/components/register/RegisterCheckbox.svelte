<script lang="typescript">
    export let label: string;
    export let group: string[] = [];
    export let value: string;
    export let id: string

    let button: HTMLInputElement;
</script>

<div class="container">
    <input {id} bind:this={button} bind:group={group}  {value} type="checkbox" class="button" checked/>
    <div class="box" on:click="{() => { button.checked = !button.checked}}"><i class="fas fa-check-square"></i></div>
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

    .box{
        width: 1rem;
        height: 1rem;
        border-radius: 3px;
        border: 1px solid var(--color-11);
    }

    .box i{ 
        display: none;
        border-radius: 3px;
    }

    input{
        position: absolute;
        width: 0px;
        height: 0px;
    }

    input:checked ~ .box{
        border: none;
    }

    input:checked ~ .box i{
        display: block;
        color: var(--color-2);
        width: 100%;
        height: 100%;
    }

    .lab{
        color: var(--color-3);
        font-family: "Roboto";
        font-size: 0.9rem;
    }
</style>
