<script lang="typescript">
    import RegisterHeader  from "../components/RegisterHeader.svelte";
    import RegisterInput from "../components/RegisterInput.svelte";
 
    let step = 1;
</script>

<aside class="form-container">
    <RegisterHeader step={step} description="Informações Pessoais"/>
    <form>
        <RegisterInput label="Nome"/>
        <RegisterInput label="Sobrenome"/>
        <RegisterInput label="E-mail"/>
    </form>
</aside>

<style>
.form-container{
    flex-grow: 1;
    height: 100%;
    background-color: var(--color-4);
}

form{
    display: grid;
    grid-template-columns: 1fr 1fr; 
    grid-template-rows: auto;
    gap: 1rem;
    width: 100%;
    justify-items: stretch;
    padding: 1rem;
}
</style>
