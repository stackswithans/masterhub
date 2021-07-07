<script lang="typescript">
    export let options: {value: string, label: string}[];
    export let group: string[] = ["1"];
    export let name: string = "aois";
    let buttons: HTMLInputElement[] = new Array(options.length);
</script>

<div class="grid-3">
    {#each options as option, i}
        <div class="container">
            <input {name} bind:this={buttons[i]} bind:group={group}  value={option.value} type="checkbox" class="button"/>
            <div class="box" on:click="{() => { buttons[i].click()}}"><i class="fas fa-check-square"></i></div>
            <label class="lab">{option.label}</label>
        </div>
    {/each}
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

    .grid-3{
        display: grid;
        grid-template-columns: 1fr 1fr 1fr; 
        grid-template-rows: auto;
        gap: 1rem;
        width: 100%;
        justify-items: stretch;
    }
</style>
