import Landing from "./routes/Landing.svelte";
import RegisterStudent from "./routes/RegisterStudent.svelte";
import RegisterMaster from "./routes/RegisterMaster.svelte";

const routes = {
    "/": Landing,
    "/register/student": RegisterStudent,
    "/register/master": RegisterMaster,
}

export default routes;
