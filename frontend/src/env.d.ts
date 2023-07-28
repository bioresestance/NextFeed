/// <reference types="vite/client" />

interface ImportMetaEnv {
    readonly VITE_DEV_CONTAINER: string | undefined
    readonly VITE_CODESPACE_NAME: string | undefined
    readonly VITE_GITHUB_DOMAIN: string | undefined
}

interface ImportMeta {
    readonly env: ImportMetaEnv
}