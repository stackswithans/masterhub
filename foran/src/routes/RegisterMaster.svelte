<script lang="typescript">
    import RegisterAside  from "../components/register/RegisterAside.svelte";
    import RegisterFormMaster  from "../components/register/RegisterFormMaster.svelte";
    import RegisterLayout  from "../components/register/RegisterLayout.svelte";
</script>


<RegisterLayout>
    <RegisterAside header="Seja bem-vindo, mestre!" src="/assets/images/register-img-2.png" alt="Girl studying"/>
    <RegisterFormMaster/>
</RegisterLayout>
