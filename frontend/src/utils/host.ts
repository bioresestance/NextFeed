


function get_host(endpoint: string, port: number = 8000): string {

    let url: string = ""

    console.log(import.meta.env.VITE_DEV_CONTAINER)

    if (import.meta.env.VITE_DEV_CONTAINER == "true") {
        url = `https://${import.meta.env.VITE_CODESPACE_NAME}-${port}.${import.meta.env.VITE_GITHUB_DOMAIN}/${endpoint}`;
    }
    else {
        url = `http://localhost:${port}/${endpoint}`;
    }
    return url;
}


export default get_host;