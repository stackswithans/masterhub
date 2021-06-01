<script lang="typescript">
    export let type: string = "text";
    export let description: string = "";
</script>

<input type="{type}" placeholder={description} class="input-after">

<style>
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

</style>
