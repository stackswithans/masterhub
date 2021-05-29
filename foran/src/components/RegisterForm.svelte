<script lang="typescript">
    import RegisterHeader  from "../components/RegisterHeader.svelte";
    import RegisterInput from "../components/RegisterInput.svelte";
    import RegisterRadio from "../components/RegisterRadio.svelte";
    import RadioGroup from "../components/RadioGroup.svelte";
 
    let step = 1;
    let options: Array<[string, string, boolean?]> = [["Masculino", "0"], ["Feminino", "1"], ["Prefiro não divulgar", "2", true] ]
    let sex: string = "1";
</script>

<aside class="form-container">
    <RegisterHeader step={step} description="Informações Pessoais"/>
    <form>
        <div class="grid">
            <RegisterInput label="Nome"/>
            <RegisterInput label="Sobrenome"/>
            <RegisterInput label="E-mail"/>
            <RegisterInput label="Telefone"/>
        </div>
        <div class="section-2">
            <h1>Gênero</h1>
            <div class="buttons">
                <RadioGroup group={sex}  {options}/>
            </div>
        </div>
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
    padding: 1rem;
}

.grid{
    display: grid;
    grid-template-columns: 1fr 1fr; 
    grid-template-rows: auto;
    gap: 1rem;
    width: 100%;
    justify-items: stretch;
}

.section-2{
    display: flex;
    flex-direction: column;
    margin-top: 1rem;
}

.section-2 h1{
    font-size: 1rem;
    margin-bottom: 1rem;
}

.section-2 .buttons{
    display: flex;
    gap: 1rem;
}
</style>
