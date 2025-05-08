import { Routes } from '@angular/router';
import { ProductListComponent } from './ecommerce/product-list/product-list.component';
import { LoginComponent } from './auth/login/login.component';
import { RegisterComponent } from './auth/register/register.component';
import { ProductSingleComponent } from './ecommerce/product-single/product-single.component';

export const routes: Routes = [
    {path: '', component: ProductListComponent},
    {path: 'login', component: LoginComponent},
    {path: 'register', component: RegisterComponent},
    {path: 'product/:id', component: ProductSingleComponent},
];
