<script lang="typescript">
    export let label = "";
    export let type: string = "text";
    export let name: string; 
    export let value = "";
    export let errors: Array<any> = [];

    let input: HTMLInputElement;

    $:{
        if(input && errors.length){
            input.style.borderColor = "red";
        }
    }
</script>

<div class="container">
    <label class="description">{label}</label>
    {#if type == "text"}
        <input name={name} bind:this={input} bind:value={value} type="text" class="input-after">
    {:else}
        <input name={name} bind:this={input} bind:value={value} type="password" class="input-after">
    {/if}
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
