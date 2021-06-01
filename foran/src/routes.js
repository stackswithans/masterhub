import Landing from "./routes/Landing.svelte";
import Login from "./routes/Login.svelte";
import RegisterStudent from "./routes/RegisterStudent.svelte";
import RegisterMaster from "./routes/RegisterMaster.svelte";

const routes = {
    "/": Landing,
    "/login": Login,
    "/register/student": RegisterStudent,
    "/register/master": RegisterMaster,
}

export default routes;
