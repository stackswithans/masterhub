<script lang="typescript">
</script>

<aside class="form-container">
    <form on:submit|preventDefault>
        <slot></slot>
    </form>
</aside>

<style>
    .form-container{
        flex-grow: 1;
        height: 100%;
        background-color: var(--color-4);
    }
    form{
        width: 100%;
        height: 100%;
        padding: 1rem;
    }
</style>
