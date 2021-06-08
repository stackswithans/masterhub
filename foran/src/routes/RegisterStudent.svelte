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

    //Form fields
    let fields = {
        "email": null, 
        "first_name": null, 
        "last_name": null, 
        "telephone":null, 
        "password":null,  
        "gender": "2",  
    };

    let errors = {
        "email": [], 
        "first_name": [], 
        "last_name": [], 
        "telephone": [], 
        "password": [],  
    };

    let step = 1;
    let steps = 2;
    let gender: string = "2";

    const nextSection = async () => {
        //Validate fields here
        if (step == 1){
            let data = {
                "utype": "ST", 
                "email": fields.email, 
                "first_name": fields.first_name, 
                "last_name": fields.last_name, 
                "telephone":fields.telephone, 
            }
            let response = await postData(reverse("users"), data);
            if(response.code == 400){
                console.log(response.body);
                for(let field in data){
                    //Get specific field errors
                    if(!response.body[field]) continue;
                    errors[field] = response.body[field];
                }
                return;
            }
        }
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
        if(response.code >= 200 && response.code <= 299){
            console.log(response.body);
        } else {
            alert("there has been an error");
            console.log(response.body);
        }
    };
</script>


<MainLayout>
    <RegisterLayout>
        <RegisterAside header="Seja bem-vindo, caro estudante!" src="/assets/images/register-img-1.png" alt="Girl studying"/>
        <RegisterForm on:submit={handleSubmit}>
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
                    <RegisterInput bind:this={fields.password} name="password" type="password" label="Palavra-passe"/>
                    <RegisterInput type="password" label="Confirm palavra-passe"/>
                    <RegisterInput label="Pergunta de segurança"/>
                    <RegisterInput label="Resposta"/>
                </div>
                <div class="footer">
                    <RegisterButton type="submit" arrow={false} text="Finalizar"/>
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
