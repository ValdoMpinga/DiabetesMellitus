function JSONParser(formData)
{
    let formObject = {};

    for (const [fieldName] of formData)
    {
        const fieldValue = formData.getAll(fieldName);
        formObject[fieldName] = fieldValue.length == 1 ? fieldValue.toString() : fieldValue
    }

    return formObject
}

export { JSONParser }
