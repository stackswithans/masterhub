<script lang="typescript">
    import RegisterAside  from "../components/register/RegisterAside.svelte";
    import RegisterForm  from "../components/register/RegisterForm.svelte";
    import RegisterLayout  from "../components/register/RegisterLayout.svelte";
</script>


<RegisterLayout>
    <RegisterAside header="Seja bem-vindo, caro estudante!" src="/assets/images/register-img-1.png" alt="Girl studying"/>
    <RegisterForm/>
</RegisterLayout>
