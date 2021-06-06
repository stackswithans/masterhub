<script lang="typescript">
    import { reverse, postFormData } from "../../scripts/utils";
    import RegisterHeader  from "./RegisterHeader.svelte";
    import RegisterInput from "./RegisterInput.svelte";
    import RegisterButton from "./RegisterButton.svelte";
    import RegisterRadio from "./RegisterRadio.svelte";
    import  FormSection from "./FormSection.svelte";

    let section1Visible = true;
    let section2Visible = false;
 
    let step = 1;
    let steps = 2;
    let gender: string = "2";

    const nextSection = () => {
        //Validate fields here
        step += 1;
        section1Visible = false;
        section2Visible = true;
    };

    const handleSubmit = async (event) => {
        console.log(event.target.email.value)
        //Validate fields here
        //let response = await postFormData(reverse("users"));
    };
</script>

<aside class="form-container">
    <form on:submit|preventDefault={handleSubmit}>
        <FormSection visible={section1Visible}>
            <RegisterHeader {steps} {step} description="Informações Pessoais"/>
            <div class="grid">
                <RegisterInput name="first_name" label="Nome"/>
                <RegisterInput name="last_name" label="Sobrenome"/>
                <RegisterInput name="email" label="E-mail"/>
                <RegisterInput name="telephone" label="Telefone"/>
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
        <FormSection visible={section2Visible}>
            <RegisterHeader {steps} {step} description="Detalhes de Acesso"/>
            <div class="grid">
                <RegisterInput name="password" type="password" label="Palavra-passe"/>
                <RegisterInput type="password" label="Confirm palavra-passe"/>
                <RegisterInput label="Pergunta de segurança"/>
                <RegisterInput label="Resposta"/>
            </div>
            <div class="footer">
                <RegisterButton type="submit" arrow={false} text="Finalizar"/>
            </div>
        </FormSection>
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
</style>
