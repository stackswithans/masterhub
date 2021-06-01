<script lang="typescript">
    import RegisterAside  from "../components/register/RegisterAside.svelte";
    import RegisterForm  from "../components/register/RegisterForm.svelte";
    import RegisterLayout  from "../components/register/RegisterLayout.svelte";
    import MainLayout  from "../components/MainLayout.svelte";
</script>


<MainLayout>
    <RegisterLayout>
        <RegisterAside header="Seja bem-vindo, caro estudante!" src="/assets/images/register-img-1.png" alt="Girl studying"/>
        <RegisterForm/>
    </RegisterLayout>
</MainLayout>
