import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, RouterLink } from '@angular/router';
import { Product, ProductService } from '../../services/product.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-product-single',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule
  ],
  templateUrl: './product-single.component.html',
  styleUrl: './product-single.component.css'
})
export class ProductSingleComponent implements OnInit {
  product: Product | null = null;
  loading: boolean = false;
  error: string = '';
  quantity: number = 1;
decrease: any;
increase: any;
addToCart: any;


  constructor(
    private route: ActivatedRoute,
    private productService: ProductService
  ) {}

  ngOnInit() {
   const id = Number(this.route.snapshot.paramMap.get('id'));
   this.productService.getById(id).subscribe({
     next: (data: Product) => {
       this.product = data;
       this.loading = false;
     }
     , error: (err: any) => {
       this.error = 'Erro ao carregar produto';
       this.loading = false;
     }

    });

}
}
