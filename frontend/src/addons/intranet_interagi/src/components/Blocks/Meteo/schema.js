// Schema do Bloco
export const blockSchema = (props) => {
  const availableMeasures = [
    ['sunrise', 'Nascer do Sol'],
    ['sunset', 'Por do Sol'],
  ];
  const defaultMeasure = 'sunset';
  return {
    title: 'Clima',
    fieldsets: [
      {
        id: 'default',
        title: 'Default',
        fields: ['header', 'measure'],
      },
    ],
    properties: {
      header: {
        title: 'Título',
        description: 'Descreve o bloco',
        widget: 'text',
      },
      measure: {
        title: 'Medida',
        description: 'O que exibir no bloco',
        choices: availableMeasures,
        default: defaultMeasure,
      },
    },
    required: ['header', 'measure'],
  };
};
