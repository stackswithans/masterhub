<script lang="typescript">
    export let label: string;
    export let group: string[] = ["1"];
    export let value: string;
    export let id: string;
    export let name: string = "aois";
    let button: HTMLInputElement;
    $: console.log(group);
</script>

<div class="container">
    <input {id} {name} bind:this={button} bind:group={group}  {value} type="checkbox" class="button"/>
    <div class="box" on:click="{() => { button.click()}}"><i class="fas fa-check-square"></i></div>
    <label for="{id}" class="lab">{label}</label>
</div>

<style>
    .container{
        display: flex;
        align-items: center;
        gap: 0.5rem;
        width: fit-content;  
        flex-wrap: nowrap;
        white-space:nowrap;
        text-overflow: ellipsis;
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
