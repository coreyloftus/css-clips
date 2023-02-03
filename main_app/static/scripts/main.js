const generateClipView = ({ html, css }) => {
    const getBlobURL = (code, type) => {
        const blob = new Blob([code], { type })
        return URL.createObjectURL(blob)
    }

    const cssURL = getBlobURL(css, "text/css")

    const source = `
        <html>
            <head>
                ${css && `<link rel="stylesheet" type="text/css" href="${cssURL}" />`}
            </head>
            <body>
                ${html || ""}
            </body>
        </html>
        `
    return getBlobURL(source, "text/html")
}
