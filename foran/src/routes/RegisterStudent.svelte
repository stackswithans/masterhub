<script lang="typescript">
    import { reverse, postData } from "../scripts/utils";
    import RegisterAside  from "../components/register/RegisterAside.svelte";
    import RegisterForm  from "../components/register/RegisterForm.svelte";
    import RegisterLayout  from "../components/register/RegisterLayout.svelte";
    import MainLayout  from "../components/MainLayout.svelte";
    import FormSection  from "../components/register/FormSection.svelte";
    import RegisterHeader  from "../components/register/RegisterHeader.svelte";
    import RegisterInput from "../components/register/RegisterInput.svelte";
    import RegisterButton from "../components/register/RegisterButton.svelte";
    import RegisterRadio from "../components/register/RegisterRadio.svelte";

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


<MainLayout>
    <RegisterLayout>
        <RegisterAside header="Seja bem-vindo, caro estudante!" src="/assets/images/register-img-1.png" alt="Girl studying"/>
        <RegisterForm>
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
        </RegisterForm>
    </RegisterLayout>
</MainLayout>

<style>
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
