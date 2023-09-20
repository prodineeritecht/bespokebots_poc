import React from 'react';

// Building blocks formControls components
import {
  IndexView as FormControlsIndexView,
  CustomSelect as CustomSelectView,
  StackedCustomRadioGroup as StackedCustomRadioGroupView,
  CustomRadioGroup as CustomRadioGroupView,
  ToggleButton as ToggleButtonView,
} from 'blocks/formControls';

const routes = [
  {
    path: '/blocks/form-controls',
    renderer: (params = {}): JSX.Element => (
      <FormControlsIndexView {...params} />
    ),
  },
  {
    path: '/blocks/form-controls/custom-select',
    renderer: (params = {}): JSX.Element => <CustomSelectView {...params} />,
  },
  {
    path: '/blocks/form-controls/stacked-custom-radio-group',
    renderer: (params = {}): JSX.Element => (
      <StackedCustomRadioGroupView {...params} />
    ),
  },
  {
    path: '/blocks/form-controls/custom-radio-group',
    renderer: (params = {}): JSX.Element => (
      <CustomRadioGroupView {...params} />
    ),
  },
  {
    path: '/blocks/form-controls/toggle-button',
    renderer: (params = {}): JSX.Element => <ToggleButtonView {...params} />,
  },
];

export default routes;
