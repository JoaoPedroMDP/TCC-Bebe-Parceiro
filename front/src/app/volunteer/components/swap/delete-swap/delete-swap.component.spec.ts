import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DeleteSwapComponent } from './delete-swap.component';

describe('DeleteSwapComponent', () => {
  let component: DeleteSwapComponent;
  let fixture: ComponentFixture<DeleteSwapComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DeleteSwapComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DeleteSwapComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
