<script lang="typescript">
    import RegisterAside  from "../components/register/RegisterAside.svelte";
    import RegisterForm from "../components/register/RegisterForm.svelte";
    import RegisterLayout  from "../components/register/RegisterLayout.svelte";
    import MainLayout  from "../components/MainLayout.svelte";
    import FormSection  from "../components/register/FormSection.svelte";
    import RegisterHeader  from "../components/register/RegisterHeader.svelte";
    import RegisterInput from "../components/register/RegisterInput.svelte";
    import RegisterButton from "../components/register/RegisterButton.svelte";
    import RegisterCheckbox from "../components/register/RegisterCheckbox.svelte";
    import RegisterRadio from "../components/register/RegisterRadio.svelte";
    import ScheduleMaker from "../components/register/ScheduleMaker.svelte";
    
    let step = 1;
    let steps = 4;
    //Gender options
    let gender: string = "1";

    //Knowledge Domain
    let categories = [
        { id: 0, description: "IOT" }, 
        { id: 1, description: "IA" }, 
        { id: 2, description: "Mecânica" }, 
        { id: 3, description: "Programação" }, 
        { id: 4, description: "Desporto" }, 
        { id: 5, description: "Saúde" }, 
    ];
    let areas: string[] = [];

    const nextSection = () => {
        //Validate fields here
        step += 1;
    };
</script>

<MainLayout>
    <RegisterLayout>
        <RegisterAside header="Seja bem-vindo, mestre!" src="/assets/images/register-img-2.png" alt="Girl studying"/>
        <RegisterForm>
            <form>
                <FormSection currentStep={step} sectionStep={1}>
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
                            <RegisterRadio label="Masculino" bind:group={gender} value="0"/>
                            <RegisterRadio label="Feminino" bind:group={gender} value="1"/>
                            <RegisterRadio label="Prefiro não divulgar" bind:group={gender} value="2" checked/>
                        </div>
                    </div>
                    <div class="footer">
                        <RegisterButton on:click={nextSection} text="Próximo passo"/>
                    </div>
                </FormSection>
                <FormSection  currentStep={step} sectionStep={2}>
                    <RegisterHeader {steps} {step} description="Quais as áreas que domina?"/>
                    <div class="grid-3">
                        {#each categories as category}
                            <RegisterCheckbox group={areas} value="{category.description}" id="master-check-{category.id}" label="{category.description}"/>
                        {/each}
                    </div>
                    <div class="footer">
                        <RegisterButton  text="Próximo passo" on:click={nextSection}/>
                    </div>
                </FormSection>
                <FormSection  currentStep={step} sectionStep={3}>
                    <RegisterHeader {steps} {step} description="Qual a sua disponibilidade?"/>
                    <div class="schedule">
                        <ScheduleMaker/>
                    </div>
                    <div class="footer">
                        <RegisterButton  text="Próximo passo" on:click={nextSection}/>
                    </div>
                </FormSection>
                <FormSection  currentStep={step} sectionStep={4}>
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
                </FormSection>
            </form>
        </RegisterForm>
    </RegisterLayout>
</MainLayout>

<style>
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
        width: 0.4rem;
        border-radius: 1rem;
    }

    .schedule::-webkit-scrollbar-thumb{
        background-color: white;
        border-radius: 1rem;
    }
</style>
