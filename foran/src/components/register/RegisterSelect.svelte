<script lang="typescript">
    export let label : string;
    export let name: string; 
    export let value = "";
    export let options = [];
    export let errors: Array<any> = [];

    let input: HTMLInputElement;

    $:{
        if(input && errors.length){
            input.style.borderColor = "red";
        }
        else if(input && !errors.length){
            input.style.borderColor = "";
        }
    }
</script>

<div class="container">
    <label class="description">{label}</label>
    <select bind:value={value} class="input-after" id="" name="">
        {#each options as option}
            <option value="{option.id}" selected>{option.degree}</option>
        {/each}
    </select>
    {#if errors.length}
    <div class="errors">
        {#each errors as error}
            <div>{error.message}</div>
        {/each}
    </div>
    {/if}
</div>

<style>
    .container{
        display: flex;
        flex-direction: column;
    }

    .description{
        position: relative;
        font-family: "Roboto";
        font-weight: bold;
        font-size: 1rem;
        color: var(--color-3);
    }

    .input-after{
        width: 100%;
        margin-top: 1rem;
        background-color: white;
        border-radius: 5px;
    }

    .input-after:focus{
        outline: none;
    }

    .errors{
        display: flex;
        flex-direction: column;
        gap: 0.3rem;
        font-family: "Roboto";
        color: red;
        font-size: 0.7rem;
    }
</style>
