<script lang="typescript">
    export let name: string;
    export let value: string;
    export let type: string = "text";
    export let description: string = "";
    export let errors = [];

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
    {#if type === "text"}
        <input {name} bind:this={input} bind:value={value} type="text" placeholder={description} class="input-after">
    {:else}
        <input {name} bind:this={input} bind:value={value} type="password" placeholder={description} class="input-after">
    {/if}
    {#if errors.length}
    <div class="errors">
        {#each errors as error}
            <div>{error.message}</div>
        {/each}
    </div>
    {:else}
    {/if}
</div>

<style>
    .container{
        display: flex;
        align-items: center;
        flex-direction: column;
        width: 100%;
    }

    .input-after{
        width: 75%;
        border-radius: 5px;
        text-indent: 1rem;
    }

    .input-after::placeholder{
        color: var(--color-6);
        font-size: 1rem;
        font-family: "Roboto Condensed";
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
