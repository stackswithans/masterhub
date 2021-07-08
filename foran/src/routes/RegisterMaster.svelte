<script lang="typescript">
    import { onMount } from "svelte";
    import { reverse, postData, getData, validateFormSection} from "../scripts/utils";
    import { push } from "svelte-spa-router";
    import { saveSessionData} from "../scripts/auth";
    import RegisterAside  from "../components/register/RegisterAside.svelte";
    import RegisterForm from "../components/register/RegisterForm.svelte";
    import RegisterLayout  from "../components/register/RegisterLayout.svelte";
    import MainLayout  from "../components/MainLayout.svelte";
    import FormSection  from "../components/register/FormSection.svelte";
    import RegisterHeader  from "../components/register/RegisterHeader.svelte";
    import RegisterInput from "../components/register/RegisterInput.svelte";
    import RegisterSelect from "../components/register/RegisterSelect.svelte";
    import RegisterButton from "../components/register/RegisterButton.svelte";
    import CheckboxGroup from "../components/register/CheckboxGroup.svelte";
    import RegisterRadio from "../components/register/RegisterRadio.svelte";
    import ScheduleMaker from "../components/register/ScheduleMaker.svelte";

    let step = 1;
    let steps = 4;

    //Knowledge Domain
    let aois = [];
    //Academic Degrees
    let degrees = [];

    onMount(async () => {
        let register_info = await (await getData(reverse("ms_register_info"))).json();
        aois = register_info.aois.map((value) => {
            return {value: value.id, label: value.description}
        });
        degrees = register_info.degree;
        //Add loading logic
    });


    //Form fields
    let fields = {
        "email": "", 
        "first_name": "", 
        "last_name": "", 
        "telephone":"", 
        "password":"",  
        "passwd_confirm": "",
        "gender": "2",  
        "occupation": "",  
        "academic_degree": "",  
        "timeslot": [[]],
        "knowledge_areas": [],
    };

    let errors = {
        "email": [], 
        "first_name": [], 
        "last_name": [], 
        "telephone": [], 
        "occupation": [],  
        "password": [],  
        "passwd_confirm": [],
    };



    const registerUser = async () => {
        let data = { "utype": "MS", ...fields };
        let response = await postData(reverse("users"), data);
        console.dir(response.body)
        if(response.ok){
            //saveSessionData(response.body);
            console.log(response.body);
        } else {
            alert("there has been an error");
        }
        return;
    };

    const nextSection = async () => {
        const validateRequired = (field: keyof typeof fields, errors) => { 
            let value = fields[field] 
            if(value !== ""){ 
                errors[field] = [];
                return [false, errors];
            }
            errors[field] = [{message:"Este campo deve ser preenchido"}];
            return [true, errors]
        }
        //Validate fields here
        let hasError: boolean = false;
        switch(step){
            case 1:{
                let s1Fields = ["first_name", "last_name", "occupation"];
                for(let field of s1Fields ){
                    [hasError, errors] = validateRequired(field as any, errors);  
                }
                errors = errors;
                console.log(fields);
                if (hasError) return;
                break;
            }
            case 2:{
                if(fields.knowledge_areas.length == 0){
                    alert("Escolha pelo menos 1 categoria!");
                    return;
                }
                console.log(fields)
                break;
            }
            case 3:{
                //Check that at least one schedule slot has been selected
                const reducer = (accumulator, currentValue) => {
                    return accumulator || currentValue;
                };
                let slotSet = fields.timeslot.map((array) => {
                    return array.reduce(reducer);
                }).reduce(reducer);
                if(!slotSet){
                    alert("Escolha pelo menos 1 vaga no horário!");
                    return;
                }  
                break;
            }
            case 4:{
                //TODO: Add loading code here
                [hasError, errors] = await validateFormSection(
                    "MS",
                    "users", 
                    fields,
                    errors,
                    ["email", "password", "passwd_confirm", "telephone"]
                );
                errors = errors;
                if (hasError) return;
                if(!(fields.password === fields.passwd_confirm)){
                    errors.passwd_confirm = errors.password =  [{message: "As palavras-passes devem ser iguais"}]; 
                    return;
                }
                errors.password = [];
                errors.passwd_confirm = [];
                console.log(fields);
                await registerUser()
                return
                break;
            }
        }
        step += 1;
    };
</script>

<MainLayout>
    <RegisterLayout>
        <RegisterAside header="Seja bem-vindo, mestre!" src="/assets/images/register-img-2.png" alt="Girl studying"/>
        <RegisterForm>
            <FormSection currentStep={step} sectionStep={1}>
                <RegisterHeader {steps} {step} description="Informações Pessoais"/>
                <div class="grid">
                    <RegisterInput errors={errors.first_name} bind:value={fields.first_name} label="Nome"/>
                    <RegisterInput errors={errors.last_name} bind:value={fields.last_name} label="Sobrenome"/>
                    <RegisterSelect bind:value={fields.academic_degree} label="Grau Académico" options={degrees}/>
                    <RegisterInput errors={errors.occupation} bind:value={fields.occupation} label="Profissão"/>
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
            <FormSection  currentStep={step} sectionStep={2}>
                <RegisterHeader {steps} {step} description="Quais as áreas que domina?"/>
                <CheckboxGroup options={aois} bind:group={fields.knowledge_areas} name="aois"/>
                <div class="footer">
                    <RegisterButton  text="Próximo passo" on:click={nextSection}/>
                </div>
            </FormSection>
            <FormSection  currentStep={step} sectionStep={3}>
                <RegisterHeader {steps} {step} description="Qual a sua disponibilidade?"/>
                <div class="schedule">
                    <ScheduleMaker bind:schedule={fields.timeslot}/>
                </div>
                <div class="footer">
                    <RegisterButton  text="Próximo passo" on:click={nextSection}/>
                </div>
            </FormSection>
            <FormSection  currentStep={step} sectionStep={4}>
                <RegisterHeader {steps} {step} description="Acesso e Contactos"/>
                <div class="grid">
                    <RegisterInput errors={errors.email} bind:value={fields.email} label="Email"/>
                    <RegisterInput errors={errors.telephone} bind:value={fields.telephone} label="Telefone"/>
                    <RegisterInput errors={errors.password} bind:value={fields.password} type="password" label="Palavra-passe"/>
                    <RegisterInput errors={errors.passwd_confirm} bind:value={fields.passwd_confirm} type="password" label="Confirmar Palavra-passe"/>
                </div>
                <div class="footer">
                    <RegisterButton on:click={nextSection} arrow={false} text="Finalizar"/>
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
