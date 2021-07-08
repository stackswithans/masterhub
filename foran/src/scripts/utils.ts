export const host = window.location.protocol + "//" + window.location.hostname;
export const clientHost = host + ":" + location.port + "/";
export const apiHost = host + ":" + "8000" + "/";

//endpoints
const endpoints = {
    students: apiHost + "api/users/students",
    masters: apiHost + "api/users/masters",
    masters_info: apiHost + "api/users/masters/register_info/",
    login: apiHost + "api/sessions/",
    call: apiHost + "call/",
    callSocket: `ws://${window.location.hostname + ":" + "8000"}/ws/call`,
};

export const postData = async (
    url = "",
    data = {}
): Promise<{ ok: boolean; code: number; body: Object }> => {
    const response = await fetch(url, {
        method: "POST",
        mode: "cors",
        cache: "no-cache",
        credentials: "same-origin",
        headers: {
            "Content-Type": "application/json",
        },
        redirect: "follow",
        referrerPolicy: "no-referrer",
        body: JSON.stringify(data),
    });

    let code: number = response.status;
    let body = await response.json();

    return { ok: response.ok, code, body };
};

export const postFormData = async (url = "", data: FormData) => {
    const response = await fetch(url, {
        method: "POST",
        mode: "cors",
        cache: "no-cache",
        credentials: "same-origin",
        headers: {
            Accept: "application/json",
        },
        redirect: "follow",
        referrerPolicy: "no-referrer",
        body: data,
    });
    return response.json();
};

export const getData = async (url = "") => {
    const response = await fetch(url, {
        method: "GET",
        mode: "cors",
        cache: "no-cache",
        credentials: "same-origin",
        headers: {
            "Content-Type": "application/json",
        },
        redirect: "follow",
        referrerPolicy: "no-referrer",
    });
    return response;
};

export const reverse = (
    path: keyof typeof endpoints,
    pathParams?: Array<string>
): string => {
    if (!(path in endpoints)) throw new Error("Invalid endpoint path name");
    if (!pathParams) pathParams = [];
    return [endpoints[path], ...pathParams].reduce(
        (accumulator, current) => accumulator + current
    );
};

export const validateFormSection = async (
    utype: string,
    path: keyof typeof endpoints,
    formData: object,
    errors: object,
    sectionFields: Array<string>
): Promise<[boolean, any]> => {
    for (let error in errors) {
        errors[error] = [];
    }
    //Get the value of the fields of this section from the form
    let data = { utype };
    sectionFields.forEach((value) => {
        data[value] = formData[value];
    });
    //Send request and get errors
    let response = await postData(reverse(path), data);
    if (!response.ok) {
        console.log(response.body);
        //Get field erros
        let hasErrors = false;
        sectionFields.forEach((field) => {
            if (!response.body[field]) return;
            hasErrors = true;
            errors[field] = response.body[field];
        });
        return [hasErrors, errors];
    }
    return [false, response.body];
};
