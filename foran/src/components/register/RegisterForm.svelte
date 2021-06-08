<script lang="typescript">
    import { reverse, postData } from "../../scripts/utils";
    import RegisterHeader  from "./RegisterHeader.svelte";
    import RegisterInput from "./RegisterInput.svelte";
    import RegisterButton from "./RegisterButton.svelte";
    import RegisterRadio from "./RegisterRadio.svelte";
    import  FormSection from "./FormSection.svelte";

 
    let step = 1;
    let steps = 2;
    let gender: string = "2";

    const nextSection = () => {
        //Validate fields here
        step += 1;
    };

    const handleSubmit = async (event) => {
        let form: HTMLFormElement = event.target;
        let data = {
            "utype": "ST", 
            "email": "stexor12@gmail.com",
            "first_name": form.first_name.value, 
            "last_name":form.last_name.value, 
            "gender": gender, 
            "telephone":form.telephone.value, 
            "password":form.password.value, 

        };
        console.log(data);
        let response = await postData(reverse("users"), data);
        console.log(response);
    };
</script>

<aside class="form-container">
    <form on:submit|preventDefault={handleSubmit}>
        <FormSection sectionStep={1} currentStep={step}>
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
        <FormSection sectionStep={2} currentStep={step}>
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
