import { Routes } from '@angular/router';
import { HomeComponent } from 'src/app/volunteer';
import { AuthGuard } from '../../guards/auth.guard';
import { ProfessionalComponent } from './professional.component';


export const ProfessionalRouting: Routes = [

  {
    path: 'professional',
    component: ProfessionalComponent, 
 
  },
];

