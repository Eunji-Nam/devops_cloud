import { useState } from 'react';

function useFieldValues(initialFieldValues) {
  const [fieldValues, setFieldValues] = useState(initialFieldValues);

  const clearFieldValus = () => setFieldValues(initialFieldValues);

  const handleChange = (e) => {
    const { name, value } = e.target;

    // setter에 값 지정
    // setFieldValues({
    //   ...fieldValues,
    //   [name]: value,
    // });

    setFieldValues((prevFieldValues) => ({
      ...prevFieldValues,
      [name]: value,
    }));
  };

  //TODO
  return [fieldValues, handleChange, clearFieldValus];
}

export default useFieldValues;
