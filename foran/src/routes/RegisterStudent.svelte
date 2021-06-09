<script lang="typescript">
    import { reverse, postData, validateFormSection} from "../scripts/utils";
    import { push } from "svelte-spa-router";
    import { saveSessionData} from "../scripts/auth";
    import RegisterAside  from "../components/register/RegisterAside.svelte";
    import RegisterForm  from "../components/register/RegisterForm.svelte";
    import RegisterLayout  from "../components/register/RegisterLayout.svelte";
    import MainLayout  from "../components/MainLayout.svelte";
    import FormSection  from "../components/register/FormSection.svelte";
    import RegisterHeader  from "../components/register/RegisterHeader.svelte";
    import RegisterInput from "../components/register/RegisterInput.svelte";
    import RegisterButton from "../components/register/RegisterButton.svelte";
    import RegisterRadio from "../components/register/RegisterRadio.svelte";

    //Form fields
    let fields = {
        "email": null, 
        "first_name": null, 
        "last_name": null, 
        "telephone":null, 
        "password":null,  
        "passwd_confirm": null,
        "gender": "2",  
    };

    let errors = {
        "email": [], 
        "first_name": [], 
        "last_name": [], 
        "telephone": [], 
        "password": [],  
        "passwd_confirm": [],
    };

    let step = 1;
    let steps = 2;

    const registerUser = async () => {
        let data = { "utype": "ST", ...fields };
        console.log(data);
        let response = await postData(reverse("users"), data);
        if(response.ok){
            saveSessionData(response.body);
            push("/home");
        } else {
            alert("there has been an error");
        }
    };

    const nextSection = async () => {
        //Validate fields here
        if (step == 1){
            let hasError: boolean;
            [hasError, errors] = await validateFormSection(
                "ST",
                fields,
                errors,
                ["email", "first_name", "last_name", "telephone", "gender"]
            );
            errors = errors;
            if(hasError) return;
        }
        else if(step == 2){
            //Check passwords match
            let hasError: boolean;
            [hasError, errors] = await validateFormSection(
                "ST", fields, errors, ["password"]
            );
            if(hasError) return;
            if(!(fields.password === fields.passwd_confirm)){
                errors.passwd_confirm = errors.password =  [{message: "As palavras-passes devem ser iguais"}]; 
                return;
            }
            errors.password = [];
            errors.passwd_confirm = [];
            registerUser();
            return
        }
        step += 1;
    };
</script>


<MainLayout>
    <RegisterLayout>
        <RegisterAside header="Seja bem-vindo, caro estudante!" src="/assets/images/register-img-1.png" alt="Girl studying"/>
        <RegisterForm>
            <FormSection sectionStep={1} currentStep={step}>
                <RegisterHeader {steps} {step} description="Informações Pessoais"/>
                <div class="grid">
                    <RegisterInput errors={errors.first_name} bind:value={fields.first_name} name="first_name" label="Nome"/>
                    <RegisterInput errors={errors.last_name} bind:value={fields.last_name} name="last_name" label="Sobrenome"/>
                    <RegisterInput errors={errors.email} bind:value={fields.email} name="email" label="E-mail"/>
                    <RegisterInput errors={errors.telephone} bind:value={fields.telephone} name="telephone" label="Telefone"/>
                </div>
                <div class="radio-group">
                    <h1>Gênero</h1>
                    <div class="buttons">
                        <RegisterRadio label="Masculino" bind:group={fields.gender} value="0"/>
                        <RegisterRadio label="Feminino" bind:group={fields.gender} value="1"/>
                        <RegisterRadio label="Prefiro não divulgar" bind:group={fields.gender} value="2" checked/>
                    </div>
                </div>
                <div class="footer">
                    <RegisterButton on:click={nextSection} text="Próximo passo"/>
                </div>
            </FormSection>
            <FormSection sectionStep={2} currentStep={step}>
                <RegisterHeader {steps} {step} description="Detalhes de Acesso"/>
                <div class="grid">
                    <RegisterInput errors={errors.password} bind:value={fields.password} name="password" type="password" label="Palavra-passe"/>
                    <RegisterInput name="passwd_confirm" type="password" errors={errors.passwd_confirm} bind:value={fields.passwd_confirm} label="Confirm palavra-passe"/>
                </div>
                <div class="footer">
                    <RegisterButton type="button" on:click={nextSection} arrow={false} text="Finalizar"/>
                </div>
            </FormSection>
        </RegisterForm>
    </RegisterLayout>
</MainLayout>

<style>
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
