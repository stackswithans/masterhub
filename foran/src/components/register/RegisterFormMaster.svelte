<script lang="typescript">
    import RegisterHeader  from "./RegisterHeader.svelte";
    import RegisterInput from "./RegisterInput.svelte";
    import RegisterButton from "./RegisterButton.svelte";
    import RadioGroup from "./RadioGroup.svelte";
    import RegisterCheckbox from "./RegisterCheckbox.svelte";
    import ScheduleMaker from "./ScheduleMaker.svelte";
 
    let step = 1;
    let steps = 3;
    //Gender options
    let options: Array<[string, string, boolean?]> = [["Masculino", "0"], ["Feminino", "1"], ["Prefiro não divulgar", "2", true]]
    let sex: string = "1";

    //Knowledge Domain
    let categories = [
        { id: 0, description: "IOT" }, 
        { id: 1, description: "IA" }, 
        { id: 2, description: "Mecânica" }, 
        { id: 3, description: "Programação" }, 
        { id: 4, description: "Desporto" }, 
        { id: 5, description: "Saúde" }, 
    ];
    let areas: string[] = ["IOT"];

    const nextSection = () => {
        //Validate fields here
        step += 1;
    };
</script>

<aside class="form-container">
    <form>
        {#if step == 1}
            <RegisterHeader {steps} {step} description="Informações Pessoais"/>
            <div class="grid">
                <RegisterInput label="Nome"/>
                <RegisterInput label="Sobrenome"/>
                <RegisterInput label="Grau Académico"/>
                <RegisterInput label="Profissão"/>
            </div>
            <div class="radio-group">
                <h1>Gênero</h1>
                <div class="buttons">
                    <RadioGroup group={sex}  {options}/>
                </div>
            </div>
            <div class="footer">
                <RegisterButton on:click={nextSection} text="Próximo passo"/>
            </div>
        {:else if step == 2}
            <RegisterHeader {steps} {step} description="Quais as áreas que domina?"/>
            <div class="grid-3">
                {#each categories as category}
                    <RegisterCheckbox group={areas} value="{category.description}" id="master-check-{category.id}" label="{category.description}"/>
                {/each}
            </div>
            <div class="footer">
                <RegisterButton  text="Próximo passo" on:click={nextSection}/>
            </div>
        {:else if step == 3}
            <RegisterHeader {steps} {step} description="Qual a sua disponibilidade?"/>
            <div class="schedule">
                <ScheduleMaker/>
            </div>
            <div class="footer">
                <RegisterButton  text="Próximo passo" on:click={nextSection}/>
            </div>
        {:else if step == 4}
            <RegisterHeader {steps} {step} description="Acesso e Contactos"/>
            <div class="grid">
                <RegisterInput label="Email"/>
                <RegisterInput label="Telefone"/>
                <RegisterInput type="password" label="Palavra-passe"/>
                <RegisterInput type="password" label="Confirmar Palavra-passe"/>
            </div>
            <div class="footer">
                <RegisterButton arrow={false} text="Finalizar"/>
            </div>
        {/if}
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

.grid{
    display: grid;
    grid-template-columns: 1fr 1fr; 
    grid-template-rows: auto;
    gap: 1rem;
    width: 100%;
    justify-items: stretch;
}

.grid-3{
    display: grid;
    grid-template-columns: 1fr 1fr 1fr; 
    grid-template-rows: auto;
    gap: 1rem;
    width: 100%;
    justify-items: stretch;
}

.radio-group{
    display: flex;
    flex-direction: column;
    margin-top: 1rem;
}

.radio-group h1{
    font-size: 1rem;
    margin-bottom: 1rem;
}

.radio-group .buttons{
    display: flex;
    gap: 1rem;
}

.footer{
    display: flex;
    margin-top: 2rem;
    justify-content: center;
}

.schedule {
    max-width: 70%;
    max-height: 70%;
    display: flex;
    overflow: auto; 
    padding-right: 1rem;
}

.schedule::-webkit-scrollbar{
    background-color: var(--color-11);
    width: 0.8svelte-routingrem;
    border-radius: 1rem;
}

.schedule::-webkit-scrollbar-thumb{
    background-color: white;
    border-radius: 1rem;
}
</style>
